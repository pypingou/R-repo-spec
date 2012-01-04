%global packname  dmt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.06
Release:          1%{?dist}
Summary:          Dependency Modeling Toolkit

Group:            Applications/Engineering 
License:          FreeBSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm R-methods R-Matrix R-MASS 

BuildRequires:    R-devel tex(latex) R-mvtnorm R-methods R-Matrix R-MASS 

%description
Probabilistic dependency modeling toolkit.

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
%doc %{rlibdir}/dmt/html
%doc %{rlibdir}/dmt/doc
%doc %{rlibdir}/dmt/NEWS
%doc %{rlibdir}/dmt/DESCRIPTION
%{rlibdir}/dmt/help
%{rlibdir}/dmt/LICENSE
%{rlibdir}/dmt/Meta
%{rlibdir}/dmt/INDEX
%{rlibdir}/dmt/NAMESPACE
%{rlibdir}/dmt/data
%{rlibdir}/dmt/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.06-1
- initial package for Fedora