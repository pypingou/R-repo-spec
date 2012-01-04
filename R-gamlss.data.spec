%global packname  gamlss.data
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.0.5
Release:          1%{?dist}
Summary:          GAMLSS Data.

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_4.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Data for GAMLSS models.

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
%doc %{rlibdir}/gamlss.data/DESCRIPTION
%doc %{rlibdir}/gamlss.data/html
%{rlibdir}/gamlss.data/INDEX
%{rlibdir}/gamlss.data/help
%{rlibdir}/gamlss.data/Meta
%{rlibdir}/gamlss.data/LICENSE
%{rlibdir}/gamlss.data/data
%{rlibdir}/gamlss.data/R
%{rlibdir}/gamlss.data/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.0.5-1
- initial package for Fedora