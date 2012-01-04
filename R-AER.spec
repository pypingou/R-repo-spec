%global packname  AER
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.8
Release:          1%{?dist}
Summary:          Applied Econometrics with R

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-car R-Formula R-lmtest R-sandwich R-strucchange R-survival R-zoo 

BuildRequires:    R-devel tex(latex) R-stats R-car R-Formula R-lmtest R-sandwich R-strucchange R-survival R-zoo 

%description
Functions, data sets, examples, demos, and vignettes for the book
Christian Kleiber and Achim Zeileis (2008), Applied Econometrics with R,
Springer-Verlag, New York. ISBN 978-0-387-77316-2. (See the vignette for a
package overview.)

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
%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.8-1
- initial package for Fedora