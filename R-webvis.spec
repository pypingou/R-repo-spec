%global packname  webvis
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Create graphics for the web from R.

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Uses Protovis to provide web graphics for R (exposes most low-level
functions).  Package is still under active development and shouldn't be
considered stable until version 0.1.  Currently uses a web browser to
process JavaScript, although future version will process JavaScript
directly and return the SVG output.  Also does not properly support
discrete labels (e.g. with histograms) or statistical functions.  See
website for more details.

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
%doc %{rlibdir}/webvis/DESCRIPTION
%doc %{rlibdir}/webvis/html
%{rlibdir}/webvis/help
%{rlibdir}/webvis/Meta
%{rlibdir}/webvis/R
%{rlibdir}/webvis/demo
%{rlibdir}/webvis/NAMESPACE
%{rlibdir}/webvis/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.2-1
- initial package for Fedora