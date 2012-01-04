%global packname  mpa
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7.3
Release:          1%{?dist}
Summary:          CoWords Method

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-network 

BuildRequires:    R-devel tex(latex) R-network 

%description
CoWords Method

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
%doc %{rlibdir}/mpa/DESCRIPTION
%doc %{rlibdir}/mpa/html
%{rlibdir}/mpa/data
%{rlibdir}/mpa/help
%{rlibdir}/mpa/INDEX
%{rlibdir}/mpa/R
%{rlibdir}/mpa/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.3-1
- initial package for Fedora