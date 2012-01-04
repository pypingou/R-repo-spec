%global packname  aod
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Analysis of Overdispersed Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-stats 

%description
This package provides a set of functions to analyse overdispersed counts
or proportions. Most of the methods are already available elsewhere but
are scattered in different packages. The proposed functions should be
considered as complements to more sophisticated methods such as
generalized estimating equations (GEE) or generalized linear mixed effect
models (GLMM).

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
%doc %{rlibdir}/aod/CITATION
%doc %{rlibdir}/aod/DESCRIPTION
%doc %{rlibdir}/aod/doc
%doc %{rlibdir}/aod/html
%{rlibdir}/aod/NAMESPACE
%{rlibdir}/aod/Meta
%{rlibdir}/aod/INDEX
%{rlibdir}/aod/R
%{rlibdir}/aod/help
%{rlibdir}/aod/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora