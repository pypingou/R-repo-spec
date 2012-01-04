%global packname  R.rsp
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.0
Release:          1%{?dist}
Summary:          Dynamic generation of scientific reports

Group:            Applications/Engineering 
License:          LGPL (>= 2.1)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-R.oo R-R.utils 

BuildRequires:    R-devel tex(latex) R-R.oo R-R.utils 

%description
An RSP document is a text-based document containing an R-embedded template
of the final document, e.g. "Today's date is <%=Sys.Date()%>".  An RSP
document is preprocessed, parsed and translated into an R script, which
when sourced generates the final document.  This way it is possible to
dynamically generate reports in plain text, HTML, TeX etc, e.g.
"\includegraphics{<%=toPDF('Normal', { curve(dnorm, from=-5, to=+5)
})%>}". It can also be used to enhance other literate programming
languages such as Sweave, e.g. "<<eval=<%=doEval%>>>= [...] @".  As
explained in one of the vignettes, RSP-embedded LaTeX vignettes can easily
be included in any R package.  In addition to RSP, this package also
provides an internal cross-platform web server and built-in dynamic
RSP-embedded HTML help pages, which can be launched by browseRsp().  If
other packages provide RSP help pages, these are automatically linked to
as well.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.0-1
- initial package for Fedora