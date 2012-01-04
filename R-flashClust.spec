%global packname  flashClust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.01
Release:          1%{?dist}
Summary:          Implementation of optimal hierarchical clustering

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Implementation of optimal hierarchical clustering

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
%doc %{rlibdir}/flashClust/DESCRIPTION
%doc %{rlibdir}/flashClust/html
%{rlibdir}/flashClust/help
%{rlibdir}/flashClust/Meta
%{rlibdir}/flashClust/INDEX
%{rlibdir}/flashClust/R
%{rlibdir}/flashClust/libs
%{rlibdir}/flashClust/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.01-1
- initial package for Fedora