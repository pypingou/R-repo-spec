%global packname  epitools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.5.6
Release:          1%{?dist}
Summary:          Epidemiology Tools

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
EpiTools: R Package for Epidemiologic Data and Graphics

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
%doc %{rlibdir}/epitools/html
%doc %{rlibdir}/epitools/DESCRIPTION
%{rlibdir}/epitools/data
%{rlibdir}/epitools/R
%{rlibdir}/epitools/Meta
%{rlibdir}/epitools/NAMESPACE
%{rlibdir}/epitools/help
%{rlibdir}/epitools/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.6-1
- initial package for Fedora