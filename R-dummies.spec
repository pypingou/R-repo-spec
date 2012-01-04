%global packname  dummies
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5.4
Release:          1%{?dist}
Summary:          Create dummy/indicator variables flexibly and efficiently

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
Expands factors, characters and other eligible classes into
dummy/indicator variables.

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
%doc %{rlibdir}/dummies/DESCRIPTION
%doc %{rlibdir}/dummies/html
%{rlibdir}/dummies/help
%{rlibdir}/dummies/Meta
%{rlibdir}/dummies/INDEX
%{rlibdir}/dummies/R
%{rlibdir}/dummies/LICENSE
%{rlibdir}/dummies/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.4-1
- initial package for Fedora