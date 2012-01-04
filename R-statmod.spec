%global packname  statmod
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.13
Release:          1%{?dist}
Summary:          Statistical Modeling

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Various statistical modeling functions including growth curve comparisons,
limiting dilution analysis, mixed linear models, heteroscedastic
regression, Tweedie family generalized linear models, the inverse-Gaussian
distribution and Gauss quadrature.

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
%doc %{rlibdir}/statmod/DESCRIPTION
%doc %{rlibdir}/statmod/doc
%doc %{rlibdir}/statmod/html
%{rlibdir}/statmod/Meta
%{rlibdir}/statmod/data
%{rlibdir}/statmod/R
%{rlibdir}/statmod/NAMESPACE
%{rlibdir}/statmod/INDEX
%{rlibdir}/statmod/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.13-1
- initial package for Fedora