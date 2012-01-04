%global packname  fastICA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.13
Release:          1%{?dist}
Summary:          FastICA Algorithms to perform ICA and Projection Pursuit

Group:            Applications/Engineering 
License:          GPL-2 | GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-13.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Implementation of FastICA algorithm to perform Independent Component
Analysis (ICA) and Projection Pursuit.

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
%doc %{rlibdir}/fastICA/DESCRIPTION
%doc %{rlibdir}/fastICA/html
%{rlibdir}/fastICA/R
%{rlibdir}/fastICA/libs
%{rlibdir}/fastICA/NAMESPACE
%{rlibdir}/fastICA/help
%{rlibdir}/fastICA/Meta
RPM build errors:
%{rlibdir}/fastICA/README
%{rlibdir}/fastICA/INDEX
%{rlibdir}/fastICA/HISTORY

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.13-1
- initial package for Fedora