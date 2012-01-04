%global packname  RadioSonde
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3
Release:          1%{?dist}
Summary:          Tools for plotting skew-T diagrams and wind profiles

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
RadioSonde is a collection of programs for reading and plotting SKEW-T,log
p diagrams and wind profiles for data collected by radiosondes (the
typical weather balloon-borne instrument), which we will call "flights",
"sondes", or "profiles" throughout the associated documentation.  The raw
data files are in a common format that has a header followed by specific
variables.  Use "help(ExampleSonde)" for the full explanation of the data

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
%doc %{rlibdir}/RadioSonde/html
%doc %{rlibdir}/RadioSonde/DESCRIPTION
%{rlibdir}/RadioSonde/INDEX
%{rlibdir}/RadioSonde/help
%{rlibdir}/RadioSonde/Meta
%{rlibdir}/RadioSonde/data
%{rlibdir}/RadioSonde/NAMESPACE
%{rlibdir}/RadioSonde/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3-1
- initial package for Fedora