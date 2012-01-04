%global packname  ExomeCNV
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Detect CNV and LOH from Exome Sequecing Data

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-DNAcopy 

BuildRequires:    R-devel tex(latex) R-DNAcopy 

%description
ExomeCNV is a statistical method to detect CNV and LOH using
depth-of-coverage and B-allele frequencies from mapped short sequence
reads in exome sequencing data.

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
%doc %{rlibdir}/ExomeCNV/html
%doc %{rlibdir}/ExomeCNV/DESCRIPTION
%{rlibdir}/ExomeCNV/R
%{rlibdir}/ExomeCNV/data
%{rlibdir}/ExomeCNV/help
%{rlibdir}/ExomeCNV/INDEX
%{rlibdir}/ExomeCNV/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora