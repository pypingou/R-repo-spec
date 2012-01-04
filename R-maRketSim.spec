%global packname  maRketSim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9
Release:          1%{?dist}
Summary:          Market simulator for R

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
maRketSim is a market simulator for R.  It was initially designed around
the bond market, with plans to expand to stocks.  maRketSim is built
around the idea of portfolios of fundmantal objects.  Therefore it is slow
in its current incarnation, but allows you the flexibility of seeing
exactly what is in your final results, since the objects are retained.

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
%doc %{rlibdir}/maRketSim/html
%doc %{rlibdir}/maRketSim/CITATION
%doc %{rlibdir}/maRketSim/DESCRIPTION
%{rlibdir}/maRketSim/data
%{rlibdir}/maRketSim/R
%{rlibdir}/maRketSim/Meta
%{rlibdir}/maRketSim/demo
%{rlibdir}/maRketSim/help
%{rlibdir}/maRketSim/NAMESPACE
%{rlibdir}/maRketSim/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9-1
- initial package for Fedora