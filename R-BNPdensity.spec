%global packname  BNPdensity
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7.8
Release:          1%{?dist}
Summary:          Ferguson-Klass type algorithm for posterior normalized random measures

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Ferguson-Klass type algorithm for porterior normalized random measures

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
%doc %{rlibdir}/BNPdensity/html
%doc %{rlibdir}/BNPdensity/DESCRIPTION
%{rlibdir}/BNPdensity/R
%{rlibdir}/BNPdensity/INDEX
%{rlibdir}/BNPdensity/data
%{rlibdir}/BNPdensity/NAMESPACE
%{rlibdir}/BNPdensity/Meta
%{rlibdir}/BNPdensity/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.8-1
- initial package for Fedora