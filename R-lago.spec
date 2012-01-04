%global packname  lago
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.1
Release:          1%{?dist}
Summary:          An efficient kernel algorithm for rare target detection and unbalanced classification

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
LAGO is a kernel method much like the SVM, except that it is constructed
without the use of any iterative optimization procedure and hence very
efficient. (Technometrics 48, 193-205; The American Statistician 62,
97-109, Sec 4.2)

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
%doc %{rlibdir}/lago/html
%doc %{rlibdir}/lago/DESCRIPTION
%{rlibdir}/lago/help
%{rlibdir}/lago/INDEX
%{rlibdir}/lago/Meta
%{rlibdir}/lago/NAMESPACE
%{rlibdir}/lago/libs
%{rlibdir}/lago/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.1-1
- initial package for Fedora