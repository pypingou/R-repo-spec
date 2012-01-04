%global packname  mra
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.7
Release:          1%{?dist}
Summary:          Analysis of Mark-Recapture data

Group:            Applications/Engineering 
License:          GNU General Public License
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Analysis of mark-recapture data using covariates. Models: CJS open
population; Huggin's closed population. Link functions: logit, sine,
hazard.  Model selection and model averaging routines. Plot methods.
Simulation routine. CJS methods produce estimates of population size using
the Horvitz-Thompson estimator.

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
%doc %{rlibdir}/mra/DESCRIPTION
%doc %{rlibdir}/mra/html
%{rlibdir}/mra/INDEX
%{rlibdir}/mra/help
%{rlibdir}/mra/data
%{rlibdir}/mra/Meta
%{rlibdir}/mra/libs
%{rlibdir}/mra/R
%{rlibdir}/mra/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.7-1
- initial package for Fedora