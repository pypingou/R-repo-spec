%global packname  labdsv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          Ordination and Multivariate Analysis for Ecology

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mgcv R-MASS 

BuildRequires:    R-devel tex(latex) R-mgcv R-MASS 

%description
A variety of ordination and vegetation analyses useful in analysis of
datasets in community ecology.  Includes many of the common ordination
methods, with graphical routines to facilitate their interpretation, as
well as several novel analyses.

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
%doc %{rlibdir}/labdsv/html
%doc %{rlibdir}/labdsv/DESCRIPTION
%{rlibdir}/labdsv/help
%{rlibdir}/labdsv/libs
%{rlibdir}/labdsv/Meta
%{rlibdir}/labdsv/data
%{rlibdir}/labdsv/ChangeLog
%{rlibdir}/labdsv/R
%{rlibdir}/labdsv/NAMESPACE
%{rlibdir}/labdsv/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.1-1
- initial package for Fedora