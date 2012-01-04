%global packname  protoclust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Hierarchical clustering with prototypes

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Performs minimax linkage hierarchical clustering.  Every cluster has an
associated prototype element that represents that cluster as described in
Bien, J., and Tibshirani, R. (2011), "Hierarchical Clustering with
Prototypes via Minimax Linkage," accepted for publication in The Journal
of the American Statistical Association, DOI: 10.1198/jasa.2011.tm10183.

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
%doc %{rlibdir}/protoclust/DESCRIPTION
%doc %{rlibdir}/protoclust/html
%{rlibdir}/protoclust/R
%{rlibdir}/protoclust/NAMESPACE
%{rlibdir}/protoclust/help
%{rlibdir}/protoclust/INDEX
%{rlibdir}/protoclust/Meta
%{rlibdir}/protoclust/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora