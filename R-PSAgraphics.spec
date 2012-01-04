%global packname  PSAgraphics
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.01
Release:          1%{?dist}
Summary:          Propensity Score Analysis Graphics

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A collection of functions that primarily produce graphics to aid in a
Propensity Score Analysis (PSA).  Functions include: cat.psa and box.psa
to test balance within strata of categorical and quantitative covariates,
circ.psa for a representation of the estimated effect size by stratum,
loess.psa that provides a graphic and loess based effect size estimate,
and various balance functions that provide measures of the balance
achieved via a PSA in a categorical covariate.

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
%doc %{rlibdir}/PSAgraphics/DESCRIPTION
%doc %{rlibdir}/PSAgraphics/CITATION
%doc %{rlibdir}/PSAgraphics/html
%{rlibdir}/PSAgraphics/data
%{rlibdir}/PSAgraphics/R
%{rlibdir}/PSAgraphics/Meta
%{rlibdir}/PSAgraphics/help
%{rlibdir}/PSAgraphics/INDEX
%{rlibdir}/PSAgraphics/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.01-1
- initial package for Fedora