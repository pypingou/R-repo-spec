%global packname  aCGH
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          Classes and functions for Array Comparative Genomic Hybridization data.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster R-survival R-multtest 
Requires:         R-Biobase R-cluster R-grDevices R-graphics R-methods R-multtest R-stats R-survival R-splines R-utils 

BuildRequires:    R-devel tex(latex) R-cluster R-survival R-multtest
BuildRequires:    R-Biobase R-cluster R-grDevices R-graphics R-methods R-multtest R-stats R-survival R-splines R-utils 


%description
Functions for reading aCGH data from image analysis output files and clone
information files, creation of aCGH S3 objects for storing these data.
Basic methods for accessing/replacing, subsetting, printing and plotting
aCGH objects.

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
%doc %{rlibdir}/aCGH/doc
%doc %{rlibdir}/aCGH/html
%doc %{rlibdir}/aCGH/DESCRIPTION
%{rlibdir}/aCGH/libs
%{rlibdir}/aCGH/Meta
%{rlibdir}/aCGH/data
%{rlibdir}/aCGH/INDEX
%{rlibdir}/aCGH/R
%{rlibdir}/aCGH/help
%{rlibdir}/aCGH/demo
%{rlibdir}/aCGH/NAMESPACE
%{rlibdir}/aCGH/examples

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora