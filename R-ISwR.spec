%global packname  ISwR
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.5
Release:          1%{?dist}
Summary:          Introductory Statistics with R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Data sets and scripts for text examples and exercises in P. Dalgaard
(2008), `Introductory Statistics with R', 2nd ed., Springer Verlag, ISBN

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
%doc %{rlibdir}/ISwR/DESCRIPTION
%doc %{rlibdir}/ISwR/html
%{rlibdir}/ISwR/data
%{rlibdir}/ISwR/Meta
%{rlibdir}/ISwR/scripts
%{rlibdir}/ISwR/R
%{rlibdir}/ISwR/help
%{rlibdir}/ISwR/INDEX
%{rlibdir}/ISwR/NAMESPACE
%{rlibdir}/ISwR/rawdata

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.5-1
- initial package for Fedora