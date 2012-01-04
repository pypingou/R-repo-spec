%global packname  RSVGTipsDevice
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          An R SVG graphics device with dynamic tips and hyperlinks

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A graphics device for R that uses the w3.org xml standard for Scalable
Vector Graphics.  This version supports tooltips with 1 to 3 lines,
hyperlinks, and line styles.

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
%doc %{rlibdir}/RSVGTipsDevice/html
%doc %{rlibdir}/RSVGTipsDevice/DESCRIPTION
%doc %{rlibdir}/RSVGTipsDevice/NEWS
%{rlibdir}/RSVGTipsDevice/help
%{rlibdir}/RSVGTipsDevice/libs
%{rlibdir}/RSVGTipsDevice/NAMESPACE
%{rlibdir}/RSVGTipsDevice/Meta
%{rlibdir}/RSVGTipsDevice/serverconfig
%{rlibdir}/RSVGTipsDevice/INDEX
%{rlibdir}/RSVGTipsDevice/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora