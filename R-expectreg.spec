%global packname  expectreg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.29
Release:          1%{?dist}
Summary:          Expectile and Quantile Regression

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mboost R-BayesX R-quadprog R-stats 
Requires:         R-splines 

BuildRequires:    R-devel tex(latex) R-mboost R-BayesX R-quadprog R-stats
BuildRequires:    R-splines 


%description
Expectile and quantile regression of models with nonlinear effects e.g.
spatial, random, ridge using least asymmetric weighed squares / absolutes
as well as boosting; also supplies expectiles for common distributions.

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
%doc %{rlibdir}/expectreg/html
%doc %{rlibdir}/expectreg/CITATION
%doc %{rlibdir}/expectreg/DESCRIPTION
%doc %{rlibdir}/expectreg/doc
%{rlibdir}/expectreg/INDEX
%{rlibdir}/expectreg/NAMESPACE
%{rlibdir}/expectreg/help
%{rlibdir}/expectreg/data
%{rlibdir}/expectreg/R
%{rlibdir}/expectreg/Meta
RPM build errors:

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.29-1
- initial package for Fedora