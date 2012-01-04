%global packname  Iso
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.10
Release:          1%{?dist}
Summary:          Functions to perform isotonic regression.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Linear order and unimodal order (univariate) isotonic regression;
bivariate isotonic regression with linear order on both variables.

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
%doc %{rlibdir}/Iso/DESCRIPTION
%doc %{rlibdir}/Iso/html
%{rlibdir}/Iso/pava.r
%{rlibdir}/Iso/Isotonic.for
%{rlibdir}/Iso/help
%{rlibdir}/Iso/unimode.r
%{rlibdir}/Iso/INDEX
%{rlibdir}/Iso/ufit.r
%{rlibdir}/Iso/Meta
%{rlibdir}/Iso/NAMESPACE
%{rlibdir}/Iso/R
%{rlibdir}/Iso/libs
%{rlibdir}/Iso/makefor

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.10-1
- initial package for Fedora