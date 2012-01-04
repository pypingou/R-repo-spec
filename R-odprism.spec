%global packname  odprism
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Optimal design and performance of random intercept and slope models.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-graphics R-lme4 R-mvtnorm 
Requires:         R-Matrix R-fields 

BuildRequires:    R-devel tex(latex) R-stats R-graphics R-lme4 R-mvtnorm
BuildRequires:    R-Matrix R-fields 


%description
Simulation functions to assess the optimal design and performance of
random intercept and slope models (i.e. mixed models), which can be used
to a priori determine adequate sampling designs for e.g. reaction norm
studies. Functions allow users to vary the sampling design in terms of
number of grouping units sampled (e.g. individuals, schools, populations,
etc.) and replicates per grouping unit (unbalanced as well balanced
datasets) and also allow users to vary the parameter conditions used to
generate the data. Subsequently, the performance of mixed models (based on
lme4 package) fitted on these datasets is assessed in terms of the
accuracy and the precision of estimates of fixed and random parameter, as
well as the statistical power.

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
%doc %{rlibdir}/odprism/html
%doc %{rlibdir}/odprism/DESCRIPTION
%{rlibdir}/odprism/data
%{rlibdir}/odprism/NAMESPACE
%{rlibdir}/odprism/INDEX
%{rlibdir}/odprism/R
%{rlibdir}/odprism/Meta
%{rlibdir}/odprism/help

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora