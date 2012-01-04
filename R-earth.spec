%global packname  earth
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          3.2.1
Release:          1%{?dist}
Summary:          Multivariate Adaptive Regression Spline Models

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_3.2-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-leaps R-plotmo R-plotrix 

BuildRequires:    R-devel tex(latex) R-leaps R-plotmo R-plotrix 

%description
Build regression models using the techniques in Friedman's papers "Fast
MARS" and "Multivariate Adaptive Regression Splines". (The term "MARS" is
copyrighted and thus not used in the name of the package.)

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2.1-1
- initial package for Fedora