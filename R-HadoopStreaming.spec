%global packname  HadoopStreaming
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Utilities for using R scripts in Hadoop streaming

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-getopt 

BuildRequires:    R-devel tex(latex) R-getopt 

%description
Provides a framework for writing map/reduce scripts for use in Hadoop
Streaming. Also facilitates operating on data in a streaming fashion,
without Hadoop.

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
%doc %{rlibdir}/HadoopStreaming/DESCRIPTION
%doc %{rlibdir}/HadoopStreaming/html
%{rlibdir}/HadoopStreaming/Meta
%{rlibdir}/HadoopStreaming/R
%{rlibdir}/HadoopStreaming/INDEX
%{rlibdir}/HadoopStreaming/help
%{rlibdir}/HadoopStreaming/wordCntDemo

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora