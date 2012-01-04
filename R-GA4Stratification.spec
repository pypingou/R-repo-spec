%global packname  GA4Stratification
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          A genetic algorithm approach to determine stratum boundaries and sample sizes of each stratum in stratified sampling

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This is a Genetic Algorithm package for the determination of the stratum
boundaries and sample sizes of each stratum in stratified sampling

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
%doc %{rlibdir}/GA4Stratification/html
%doc %{rlibdir}/GA4Stratification/DESCRIPTION
%{rlibdir}/GA4Stratification/INDEX
%{rlibdir}/GA4Stratification/Meta
%{rlibdir}/GA4Stratification/NAMESPACE
%{rlibdir}/GA4Stratification/R
%{rlibdir}/GA4Stratification/help
%{rlibdir}/GA4Stratification/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora