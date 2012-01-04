%global packname  fgac
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6.1
Release:          1%{?dist}
Summary:          Generalized Archimedean Copula

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.6-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Bi-variate data fitting is done by two stochastic components: the marginal
distributions and the dependency structure. The dependency structure is
modeled through a copula. An algorithm was implemented considering seven
families of copulas (Generalized Archimedean Copulas), the best fitting
can be obtained looking all copula's options (totally positive of order 2
and stochastically increasing models).

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
%doc %{rlibdir}/fgac/html
%doc %{rlibdir}/fgac/DESCRIPTION
%{rlibdir}/fgac/NAMESPACE
%{rlibdir}/fgac/help
%{rlibdir}/fgac/Meta
%{rlibdir}/fgac/INDEX
%{rlibdir}/fgac/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6.1-1
- initial package for Fedora