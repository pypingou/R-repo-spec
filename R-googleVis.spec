%global packname  googleVis
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.11
Release:          1%{?dist}
Summary:          Interface between R and the Google Visualisation API

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-RJSONIO R-methods R-utils 

BuildRequires:    R-devel tex(latex) R-RJSONIO R-methods R-utils 

%description
googleVis provides an interface between R and the Google Visualisation API
to create interactive charts. The functions of the package allow the user
to visualise data stored in R data frames with the Google Visualisation
API in a web browser, without uploading the data to Google. The output of
a googleVis function is html code that contains the data and references to
JavaScript functions hosted by Google. googleVis makes use of the internal
R HTTP server to display the output locally, e.g. http://localhost/. A
browser with Flash and Internet connection is required. Please visit the
project web site for more information and examples.

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
%doc %{rlibdir}/googleVis/doc
%doc %{rlibdir}/googleVis/DESCRIPTION
%doc %{rlibdir}/googleVis/html
%doc %{rlibdir}/googleVis/NEWS
%{rlibdir}/googleVis/demo
%{rlibdir}/googleVis/help
%{rlibdir}/googleVis/NAMESPACE
%{rlibdir}/googleVis/LICENSE
%{rlibdir}/googleVis/INDEX
%{rlibdir}/googleVis/data
%{rlibdir}/googleVis/R
%{rlibdir}/googleVis/brew
%{rlibdir}/googleVis/rsp
%{rlibdir}/googleVis/gadgets
%{rlibdir}/googleVis/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.11-1
- initial package for Fedora