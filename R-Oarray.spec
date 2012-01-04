%global packname  Oarray
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4.3
Release:          1%{?dist}
Summary:          Arrays with arbitrary offsets

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Generalise the starting point of the array index

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
%doc %{rlibdir}/Oarray/html
%doc %{rlibdir}/Oarray/DESCRIPTION
%{rlibdir}/Oarray/INDEX
%{rlibdir}/Oarray/NAMESPACE
%{rlibdir}/Oarray/R
%{rlibdir}/Oarray/Meta
%{rlibdir}/Oarray/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.3-1
- initial package for Fedora