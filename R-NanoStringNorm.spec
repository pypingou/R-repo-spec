%global packname  NanoStringNorm
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Normalize NanoString miRNA and mRNA data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The function is used to Normalize Nanostring data

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
%doc %{rlibdir}/NanoStringNorm/html
%doc %{rlibdir}/NanoStringNorm/DESCRIPTION
%{rlibdir}/NanoStringNorm/help
%{rlibdir}/NanoStringNorm/NAMESPACE
%{rlibdir}/NanoStringNorm/unitTests
%{rlibdir}/NanoStringNorm/extdata
%{rlibdir}/NanoStringNorm/data
%{rlibdir}/NanoStringNorm/R
%{rlibdir}/NanoStringNorm/INDEX
%{rlibdir}/NanoStringNorm/Meta
%{rlibdir}/NanoStringNorm/scripts

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.7-1
- initial package for Fedora