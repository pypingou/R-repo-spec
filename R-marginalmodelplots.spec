%global packname  marginalmodelplots
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Marginal Mean Model Plots

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-locfit R-grid 

BuildRequires:    R-devel tex(latex) R-locfit R-grid 

%description
Marginal mean model plots for linear (lm) and generalized linear models
(glm).  Including tools for bandwidth exploration.  Built on the work from
the alr3 and locfit packages.

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
%doc %{rlibdir}/marginalmodelplots/html
%doc %{rlibdir}/marginalmodelplots/DESCRIPTION
%{rlibdir}/marginalmodelplots/help
%{rlibdir}/marginalmodelplots/data
%{rlibdir}/marginalmodelplots/INDEX
%{rlibdir}/marginalmodelplots/Meta
%{rlibdir}/marginalmodelplots/NAMESPACE
%{rlibdir}/marginalmodelplots/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.2-1
- initial package for Fedora