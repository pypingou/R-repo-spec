%global packname  ChemmineR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.6.0
Release:          1%{?dist}
Summary:          Analysis of Small Molecule and Screening Data

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 
Requires:         R-graphics R-methods R-stats R-RCurl 

BuildRequires:    R-devel tex(latex) R-methods
BuildRequires:    R-graphics R-methods R-stats R-RCurl 


%description
ChemmineR is an R package for analyzing small molecule and screening data.
The new version of the package 'ChemmineR-V2' contains efficient functions
and data containers for processing SDFs (structure data files), structural
similarity searching, clustering/diversity analyses of compound libraries
with a wide spectrum of algorithms. In addition, it offers utilities for
managing complex data sets from high-throughput compound bio-assays, and
visualization functions for clustering results and chemical structures.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.6.0-1
- initial package for Fedora