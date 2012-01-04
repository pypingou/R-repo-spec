%global packname  locfdr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.7
Release:          1%{?dist}
Summary:          Computes local false discovery rates

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-splines 

BuildRequires:    R-devel tex(latex) R-splines 

%description
Computation of local false discovery rates

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
%doc %{rlibdir}/locfdr/DESCRIPTION
%doc %{rlibdir}/locfdr/doc
%doc %{rlibdir}/locfdr/html
%{rlibdir}/locfdr/INDEX
%{rlibdir}/locfdr/help
%{rlibdir}/locfdr/Meta
%{rlibdir}/locfdr/data
%{rlibdir}/locfdr/NAMESPACE
%{rlibdir}/locfdr/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.7-1
- initial package for Fedora