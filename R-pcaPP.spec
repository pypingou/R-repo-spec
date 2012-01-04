%global packname  pcaPP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9.44
Release:          1%{?dist}
Summary:          Robust PCA by Projection Pursuit

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.9-44.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mvtnorm 

BuildRequires:    R-devel tex(latex) R-mvtnorm 

%description
Robust PCA by Projection Pursuit

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
%doc %{rlibdir}/pcaPP/DESCRIPTION
%doc %{rlibdir}/pcaPP/doc
%doc %{rlibdir}/pcaPP/html
%{rlibdir}/pcaPP/libs
%{rlibdir}/pcaPP/help
%{rlibdir}/pcaPP/Meta
%{rlibdir}/pcaPP/R
%{rlibdir}/pcaPP/NAMESPACE
%{rlibdir}/pcaPP/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.44-1
- initial package for Fedora