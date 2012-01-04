%global packname  hacks
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.9
Release:          1%{?dist}
Summary:          Convenient R Functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-9.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains useful functions.

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
%doc %{rlibdir}/hacks/html
%doc %{rlibdir}/hacks/DESCRIPTION
%{rlibdir}/hacks/NAMESPACE
%{rlibdir}/hacks/INDEX
%{rlibdir}/hacks/R
%{rlibdir}/hacks/help
%{rlibdir}/hacks/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.9-1
- initial package for Fedora