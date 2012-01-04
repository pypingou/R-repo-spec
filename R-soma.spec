%global packname  soma
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          General-purpose optimisation with the Self-Organising Migrating Algorithm

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-reportr 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-reportr 


%description
This package provides an R implementation of the Self-Organising Migrating
Algorithm, a general-purpose, stochastic optimisation algorithm. The
approach is similar to that of genetic algorithms, although it is based on
the idea of a series of ``migrations'' by a fixed set of individuals,
rather than the development of successive generations. It can be applied
to any cost-minimisation problem with a bounded parameter space, and is
robust to local minima.

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
%doc %{rlibdir}/soma/NEWS
%doc %{rlibdir}/soma/LICENCE
%doc %{rlibdir}/soma/html
%doc %{rlibdir}/soma/DESCRIPTION
%{rlibdir}/soma/Meta
%{rlibdir}/soma/INDEX
%{rlibdir}/soma/R
%{rlibdir}/soma/NAMESPACE
%{rlibdir}/soma/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora