%global packname  factDesign
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.30.0
Release:          1%{?dist}
Summary:          Factorial designed microarray experiment analysis

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 

BuildRequires:    R-devel tex(latex) R-Biobase 

%description
This package provides a set of tools for analyzing data from a factorial
designed microarray experiment, or any microarray experiment for which a
linear model is appropriate. The functions can be used to evaluate tests
of contrast of biological interest and perform single outlier detection.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.30.0-1
- initial package for Fedora