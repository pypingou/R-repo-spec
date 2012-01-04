%global packname  nor1mix
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.3
Release:          1%{?dist}
Summary:          Normal (1-d) Mixture Models (S3 Classes and Methods)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-graphics 

BuildRequires:    R-devel tex(latex) R-stats R-graphics 

%description
Onedimensional Normal Mixture Models Classes, for, e.g., density
estimation or clustering algorithms research and teaching; providing the
widely used Marron-Wand densities, see ?MarronWand.

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
%doc %{rlibdir}/nor1mix/DESCRIPTION
%doc %{rlibdir}/nor1mix/html
%{rlibdir}/nor1mix/NAMESPACE
%{rlibdir}/nor1mix/INDEX
%{rlibdir}/nor1mix/Meta
%{rlibdir}/nor1mix/help
%{rlibdir}/nor1mix/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.3-1
- initial package for Fedora