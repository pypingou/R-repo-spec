%global packname  contrast
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.16
Release:          1%{?dist}
Summary:          A collection of contrast methods

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rms 


BuildRequires:    R-devel tex(latex) R-rms



%description
Contrast methods, in the style of the Design package, for fit objects
produced by the lm, glm, gls, and geese functions.

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
%doc %{rlibdir}/contrast/html
%doc %{rlibdir}/contrast/doc
%doc %{rlibdir}/contrast/DESCRIPTION
%{rlibdir}/contrast/R
%{rlibdir}/contrast/Meta
%{rlibdir}/contrast/NAMESPACE
%{rlibdir}/contrast/help
%{rlibdir}/contrast/INDEX
%{rlibdir}/contrast/CHANGES

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.16-1
- initial package for Fedora