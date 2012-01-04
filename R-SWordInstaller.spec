%global packname  SWordInstaller
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          SWord: Use R in Microsoft Word (Installer)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rscproxy R-rcom 


BuildRequires:    R-devel tex(latex) R-rscproxy R-rcom



%description
Creating articles and reports in Word is easy. Adding R results (figures,
tables, summaries) requires manually copying the data from R to Word.
Changing the data requires redoing the analyses in R and re-inserting the
results into Word manually. SWord integrates R scripts and results into
Word documents. Documents can be edited and read even without R installed
(or without any knowledge of R). The functionality of embedding the
scripts is somewhat similar to what Sweave does for LaTeX documents. In
addition, the R results become part of the same document. R results can be
textual results (e.g., the output of an object "summary"), tables (e.g.,
the values of a data frame) or figures (plots, graphs).

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora