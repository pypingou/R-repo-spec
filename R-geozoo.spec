%global packname  geozoo
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.4.2
Release:          1%{?dist}
Summary:          Zoo of Geometric Objects

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-bitops R-tourr 

BuildRequires:    R-devel tex(latex) R-bitops R-tourr 

%description
The package allows geometric objects defined in geozoo to be displayed in
GGobi through the use of rggobi.

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
%doc %{rlibdir}/geozoo/DESCRIPTION
%doc %{rlibdir}/geozoo/NEWS
%doc %{rlibdir}/geozoo/html
%{rlibdir}/geozoo/INDEX
%{rlibdir}/geozoo/NAMESPACE
%{rlibdir}/geozoo/help
%{rlibdir}/geozoo/R
%{rlibdir}/geozoo/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.2-1
- initial package for Fedora