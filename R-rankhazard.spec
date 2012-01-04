%global packname  rankhazard
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8
Release:          1%{?dist}
Summary:          Rank-hazard plots

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Rank-hazard plots (Karvanen and Harrell, Statistics in Medicine 2009)
visualize the relative importance of covariates in a proportional hazards
model. The key idea is to rank the covariate values and plot the relative
hazard as a function of ranks scaled to interval [0,1]. The relative
hazard is plotted with respect to the reference hazard, which can be e.g.
the hazard related to the median of the covariate. Transformation to
scaled ranks allows plotting of covariates measured in different units in
the same graph, which helps in the interpretation of the epidemiological
relevance of the covariates. Rank-hazard plots show the difference of
hazards between the extremes of the covariate values present in the data
and can be used as a tool to check if the proportional hazards assumption
leads to reasonable estimates for individuals with extreme covariate
values. Alternative covariate definitions or different transformations
applied to covariates can be also compared using rank-hazard plots.

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
%doc %{rlibdir}/rankhazard/DESCRIPTION
%doc %{rlibdir}/rankhazard/html
%{rlibdir}/rankhazard/Meta
%{rlibdir}/rankhazard/INDEX
%{rlibdir}/rankhazard/help
%{rlibdir}/rankhazard/NAMESPACE
%{rlibdir}/rankhazard/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8-1
- initial package for Fedora