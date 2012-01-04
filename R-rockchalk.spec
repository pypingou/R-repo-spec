%global packname  rockchalk
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Regression Estimation and Presentation

Group:            Applications/Engineering 
License:          GPL (>= 3.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-car 

BuildRequires:    R-devel tex(latex) R-MASS R-car 

%description
A collection of functions for ease of presentation and interpretation of
regression analysis. See the outreg function for a way to generate LaTeX
tables of regression models and mcGraph for creating 3-dimensional
regression plots. The package title "rockchalk" refers to the expression,
"Rock Chalk Jayhawk, Go K.U.".

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
%doc %{rlibdir}/rockchalk/DESCRIPTION
%doc %{rlibdir}/rockchalk/html
%{rlibdir}/rockchalk/help
%{rlibdir}/rockchalk/Meta
%{rlibdir}/rockchalk/NAMESPACE
%{rlibdir}/rockchalk/R
%{rlibdir}/rockchalk/ChangeLog
%{rlibdir}/rockchalk/data
%{rlibdir}/rockchalk/centeredRegression.R
%{rlibdir}/rockchalk/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora