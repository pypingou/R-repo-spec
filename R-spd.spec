%global packname  spd
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6
Release:          1%{?dist}
Summary:          Semi Parametric Distribution

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-graphics R-KernSmooth 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-KernSmooth 

%description
Semi Parametric Piecewise Distribution

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
%doc %{rlibdir}/spd/html
%doc %{rlibdir}/spd/DESCRIPTION
%{rlibdir}/spd/help
%{rlibdir}/spd/Meta
%{rlibdir}/spd/R
%{rlibdir}/spd/INDEX
%{rlibdir}/spd/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6-1
- initial package for Fedora