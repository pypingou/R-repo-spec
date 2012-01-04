%global packname  argosfilter
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.62
Release:          1%{?dist}
Summary:          Argos locations filter

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions to filters animal satellite tracking data obtained from Argos.
It is especially indicated for telemetry studies of marine animals, where
Argos locations are predominantly of low-quality.

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
%doc %{rlibdir}/argosfilter/DESCRIPTION
%doc %{rlibdir}/argosfilter/html
%{rlibdir}/argosfilter/NAMESPACE
%{rlibdir}/argosfilter/Meta
%{rlibdir}/argosfilter/help
%{rlibdir}/argosfilter/INDEX
%{rlibdir}/argosfilter/data
%{rlibdir}/argosfilter/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.62-1
- initial package for Fedora