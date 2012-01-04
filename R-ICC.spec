%global packname  ICC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          Functions facilitating the estimation of the Intraclass Correlation Coefficient

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The package includes a number of functions to assist in the estimation of
the Intraclass Correlation Coefficient (ICC). Functions included estimate
the ICC from variance components of a one-way ANOVA and also estimate the
number of individuals or groups necessary to obtain an ICC estimate with a
desired confidence interval width.

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
%doc %{rlibdir}/ICC/html
%doc %{rlibdir}/ICC/CITATION
%doc %{rlibdir}/ICC/DESCRIPTION
%{rlibdir}/ICC/R
%{rlibdir}/ICC/NAMESPACE
%{rlibdir}/ICC/help
%{rlibdir}/ICC/INDEX
%{rlibdir}/ICC/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora