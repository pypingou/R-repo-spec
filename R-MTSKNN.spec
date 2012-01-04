%global packname  MTSKNN
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Multivariate two-sample tests based on K-nearest-neighbors

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The package contains four multivariate two-sample tests which are all
based on k-nearest-neighbors. The testing procedures are distribution free
and are robust from balanced designs to unbalanced designs.

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
%doc %{rlibdir}/MTSKNN/DESCRIPTION
%doc %{rlibdir}/MTSKNN/html
%{rlibdir}/MTSKNN/libs
%{rlibdir}/MTSKNN/R
%{rlibdir}/MTSKNN/INDEX
%{rlibdir}/MTSKNN/help
%{rlibdir}/MTSKNN/NAMESPACE
%{rlibdir}/MTSKNN/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.5-1
- initial package for Fedora