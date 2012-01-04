%global packname  eigenmodel
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Semiparametric factor and regression models for symmetric relational data

Group:            Applications/Engineering 
License:          GPL Version 2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package estimates the parameters of a model for symmetric relational
data (e.g.,  the above-diagonal part of a square matrix), using a
model-based eigenvalue decomposition and regression. Missing data is
accomodated, and a posterior mean for missing data is calculated under the
assumption that the data are missing at random. The marginal distribution
of the relational data can be arbitrary, and is fit with an ordered probit

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
%doc %{rlibdir}/eigenmodel/html
%doc %{rlibdir}/eigenmodel/DESCRIPTION
%{rlibdir}/eigenmodel/Meta
%{rlibdir}/eigenmodel/data
%{rlibdir}/eigenmodel/R
%{rlibdir}/eigenmodel/INDEX
%{rlibdir}/eigenmodel/NAMESPACE
%{rlibdir}/eigenmodel/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora