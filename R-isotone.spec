%global packname  isotone
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Active set and generalized PAVA for isotone optimization

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package contains two main functions: gpava() for solving general
isotone regression problem using the pool-adjacent-violators algorithm
(PAVA). activeSet() provides a framework of active set methods for isotone
optimization problems with arbitrary order restrictions. Various types of
loss functions are pre-spcified.

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
%doc %{rlibdir}/isotone/html
%doc %{rlibdir}/isotone/doc
%doc %{rlibdir}/isotone/DESCRIPTION
%doc %{rlibdir}/isotone/CITATION
%{rlibdir}/isotone/INDEX
%{rlibdir}/isotone/NAMESPACE
%{rlibdir}/isotone/help
%{rlibdir}/isotone/data
%{rlibdir}/isotone/R
%{rlibdir}/isotone/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora