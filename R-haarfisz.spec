%global packname  haarfisz
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.5
Release:          1%{?dist}
Summary:          Software to perform Haar Fisz transforms

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-wavethresh 

BuildRequires:    R-devel tex(latex) R-wavethresh 

%description
A Haar-Fisz algorithm for Poisson intensity estimation

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
%doc %{rlibdir}/haarfisz/html
%doc %{rlibdir}/haarfisz/DESCRIPTION
%{rlibdir}/haarfisz/NAMESPACE
%{rlibdir}/haarfisz/Meta
%{rlibdir}/haarfisz/R
%{rlibdir}/haarfisz/INDEX
%{rlibdir}/haarfisz/data
%{rlibdir}/haarfisz/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.5-1
- initial package for Fedora